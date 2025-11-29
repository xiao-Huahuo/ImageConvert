from PIL import Image

def jpg_to_jpeg(input_path, output_path):
    """Converts JPG to JPEG."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'jpeg')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 JPG 转换为 JPEG 时出错: {e}"

def jpeg_to_jpg(input_path, output_path):
    """Converts JPEG to JPG."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'jpeg') # 'jpg' is not a valid save format, use 'jpeg'
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 JPEG 转换为 JPG 时出错: {e}"
