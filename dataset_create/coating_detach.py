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
category_labels = {    
    "薄白润苔": 0,    
    "薄白滑苔": 1,    
    "白腻苔": 2,    
    "白滑腻苔": 3,    
    "白粘腻苔": 4,    
    "白厚腻苔": 5,    
    "白厚松苔": 6,    
    "白腻苔化燥": 7,    
    "黄腻苔化燥": 8,    
    "薄黄苔": 9,    
    "黄腻苔": 10,    
    "黄粘腻苔": 11,    
    "黄滑苔": 12,    
    "黄燥苔": 13,    
    "黄瓣苔": 14,    
    "灰白腻苔": 15,    
    "灰黄腻苔": 16,    
    "垢腻灰苔": 17,    
    "黑腻苔": 18,    
    "焦黑苔": 19,    
    "黑燥苔": 20,    
    "剥苔": 21,    
    "腻苔中剥": 22,    
    "类剥苔": 23,    
    "地图舌": 24,    
    "镜面苔": 25,    
    "无根苔": 26
    }

# 处理图片并生成增强图像与标签文件
def process_images(input_root, output_root, labels_root):
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
                if category not in category_labels:
                    print(f"警告：类别 {category} 未定义标签，跳过该文件夹")
                    continue
                
                category_label = category_labels[category]

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
    input_folder = "img_coating"  # 原始图片目录
    output_folder = "images_coating"  # 处理后的图片保存目录
    labels_folder = "labels_coating"  # 标签保存目录

    process_images(input_folder, output_folder, labels_folder)

