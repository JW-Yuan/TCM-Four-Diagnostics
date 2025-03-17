from PIL import Image
from tongue_detect.YoloModel import YOLO_model

#注意这里将所有警告忽略了
import warnings
warnings.simplefilter("ignore", UserWarning)

from PIL import Image, ImageEnhance

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




if __name__=="__main__":
    # 实例化 YOLO 类
    tongue_model = YOLO_model()
    # 打开单张图片，这里无论是cv2读取还是pil读取都可以，都会进入detect_single_image后变为PIL图片形式
    image_path = '1.jpg'
    image = Image.open(image_path)


    # 调用 detect_single_image 方法进行目标检测
    detected_image,bbox,conf,crop_img= tongue_model.detect_single_image(image,crop=True)

    if detected_image is None:
        print("********************************")
        print("没有舌像")
        print("********************************")
    else:
        print("********************************")
        print("舌像存在")
        print("********************************")
        # # 保存检测后的图片
        save_path = 'detected_image.jpg' 
        detected_image.save(save_path)
        print(f"检测后的图片已保存到 {save_path}")
        # # 保存裁剪后的舌像图片
        crop_path = 'crop_image.jpg' 
        crop_img.save(crop_path)
        print(f"裁剪后的图片已保存到 {crop_path}")
        # # 增强图像
        resize_img=enhance_cropped_image_pil(crop_img)
        resize_path="增强图像.jpg"
        resize_img.save(resize_path)
        print(f"增强后的舌像已保存到 {resize_path}")
        # # 打印置信度和边界框
        print(f"置信度为 {conf}")
        print(f"边界框为{bbox}")




    