import os
from PIL import Image
from PIL import Image, ImageEnhance
# from shutil import copy2

# 假设 YOLO_model 和 enhance_cropped_image_pil 方法已定义
from tongue_detect.YoloModel import YOLO_model



def enhance_cropped_image_pil(pil_img, upscale_factor=4, sharpness_factor=2,contrast_factor=1.0):
    # 裁剪图像
    cropped_image = pil_img

    # 放大图像（使用 LANCZOS 进行高质量插值）
    new_size = (cropped_image.width * upscale_factor, cropped_image.height * upscale_factor)
    cropped_image = cropped_image.resize(new_size, Image.LANCZOS)

    # 增强锐度
    sharpness_enhancer = ImageEnhance.Sharpness(cropped_image)
    cropped_image = sharpness_enhancer.enhance(sharpness_factor)

    # 可选：提升对比度
    contrast_enhancer = ImageEnhance.Contrast(cropped_image)
    cropped_image = contrast_enhancer.enhance(contrast_factor)

    return cropped_image




# 定义类别标签映射
COLOR_MAP = {
    "淡红舌": 0,
    "淡白舌": 1,
    "枯白舌": 2,
    "红舌": 3,
    "绛舌": 4,
    "舌尖红": 5,
    "舌边尖红": 6,
    "青紫舌": 7,
    "淡紫舌": 8,
    "瘀斑舌": 9,
    "瘀点舌": 10
}

SHAPE_MAP = {
    "老舌": 0,
    "淡嫩舌": 1,
    "红嫩舌": 2,
    "胖大舌": 3,
    "淡胖舌": 4,
    "肿胀舌": 5,
    "齿痕舌": 6,
    "红瘦舌": 7,
    "淡瘦舌": 8,
    "红点舌": 9,
    "芒刺舌": 10,
    "裂纹舌": 11,
    "淡裂舌": 12,
    "红裂舌": 13,
    "舌衄": 14,
    "舌疮": 15
}

COATING_COLOR_MAP = {
    "白苔": 0,
    "薄白润苔": 1,
    "薄白干苔": 2,
    "薄白滑苔": 3,
    "白厚苔": 4,
    "白厚腻苔": 5,
    "白厚腻干苔": 6,
    "积粉苔": 7,
    "白燥苔": 8,
    "黄苔": 9,
    "薄黄苔": 10,
    "深黄苔": 11,
    "焦黄苔": 12,
    "黄糙苔": 13,
    "黄滑苔": 14,
    "黄腻苔": 15,
    "黄黏腻苔": 16,
    "灰黑苔": 17,
    "灰黑腻润苔": 18,
    "灰黑干燥苔": 19,
    "相兼苔色": 20,
    "黄白相兼苔": 21,
    "黑（灰）白相兼苔": 22,
    "黄腻黑（灰）相兼苔": 23
}

COATING_TEXTURE_MAP = {
    "薄苔": 0,
    "厚苔": 1,
    "润苔": 2,
    "滑苔": 3,
    "燥苔": 4,
    "糙苔": 5,
    "腻苔": 6,
    "垢腻苔": 7,
    "黏腻苔": 8,
    "滑腻苔": 9,
    "燥腻苔": 10,
    "腐苔": 11,
    "脓腐苔": 12,
    "白霉苔": 13,
    "剥苔": 14,
    "淡剥苔": 15,
    "红剥苔": 16,
    "花剥苔": 17,
    "类剥苔": 18,
    "地图舌": 19,
    "镜面舌": 20,
    "镜面红舌": 21,
    "镜面淡舌": 22
}

CONDITION_MAP = {
    "正常舌态": 0,
    "舌歪斜": 1,
    "舌僵硬": 2,
    "舌痿软": 3,
    "舌短缩": 4,
    "舌吐弄": 5,
    "舌震颤": 6
}

STATUS_MAP = {
    "荣舌": 0,
    "枯舌": 1
}

VEIN_MAP = {
    "正常舌脉": 0,
    "舌脉粗长如网": 1,
    "舌脉曲张": 2,
    "舌脉瘀血": 3
}



# 处理图片并生成增强图像与标签文件
def process_images(input_root, output_root, labels_root,category_map):
    # 实例化 YOLO 模型
    tongue_model = YOLO_model()
    
    # 确保输出目录存在
    os.makedirs(output_root, exist_ok=True)
    os.makedirs(labels_root, exist_ok=True)

    # 遍历 "img" 文件夹的 test/train/val 目录
    for dataset_split in os.listdir(input_root):  # 遍历 test、train、val
        dataset_split_path = os.path.join(input_root, dataset_split)
        output_dataset_split_path = os.path.join(output_root, dataset_split)
        labels_dataset_split_path = os.path.join(labels_root, dataset_split)

        if not os.path.isdir(dataset_split_path):
            continue

        os.makedirs(output_dataset_split_path, exist_ok=True)
        os.makedirs(labels_dataset_split_path, exist_ok=True)

        # 进入 test/train/val 目录，查找具体的舌诊类别
        for category in os.listdir(dataset_split_path):
            category_path = os.path.join(dataset_split_path, category)
            output_category_path = os.path.join(output_dataset_split_path, category)
            label_category_path = os.path.join(labels_dataset_split_path, category)

            if os.path.isdir(category_path):
                os.makedirs(output_category_path, exist_ok=True)
                os.makedirs(label_category_path, exist_ok=True)

                # 获取类别标签，如果不在映射表中，则跳过
                if category not in category_map:
                    print(f"警告：类别 {category} 未定义标签，跳过该文件夹")
                    continue
                
                category_label = category_map[category]

                image_counter = 1  # 计数器，用于命名图片和对应的txt文件

                for image_name in os.listdir(category_path):  # 直接遍历图片
                    image_path = os.path.join(category_path, image_name)

                    # 只处理图片
                    if not image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                        continue
                    
                    try:
                        image = Image.open(image_path)
                        # 目标检测
                        detected_image, bbox, conf, crop_img = tongue_model.detect_single_image(image, crop=True)

                        if detected_image is None:
                            print(f"跳过 {image_name}（未检测到舌像）")
                            continue

                        # 增强舌像
                        enhanced_img = enhance_cropped_image_pil(crop_img)

                        # 生成新的文件名
                        new_image_name = f"{image_counter}.jpg"
                        output_image_path = os.path.join(output_category_path, new_image_name)
                        
                        # 对应的标签文件路径
                        label_file_name = f"{image_counter}.txt"
                        label_file_path = os.path.join(label_category_path, label_file_name)

                        # 保存增强后的图片
                        enhanced_img.save(output_image_path)
                        print(f"已处理 {image_name}，增强后保存为 {output_image_path}")

                        # 生成标签文件
                        with open(label_file_path, "w") as label_file:
                            label_content = f"{category_label} 0.5 0.5 1 1"
                            label_file.write(label_content)

                        print(f"标签文件 {label_file_path} 已生成：{label_content}")

                        image_counter += 1  # 计数器递增

                    except Exception as e:
                        print(f"处理 {image_name} 时出错: {e}")



if __name__ == "__main__":
    input_folder = "shape_dataset"  # 原始图片目录
    output_folder = "shape_img"  # 处理后的图片保存目录
    labels_folder = "shape_label"  # 标签保存目录
    category_map = SHAPE_MAP
    process_images(input_folder, output_folder, labels_folder,category_map)

