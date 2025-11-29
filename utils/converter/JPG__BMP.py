from PIL import Image

def jpg_to_bmp(input_path, output_path):
    """Converts JPG to BMP."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'bmp')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 JPG 转换为 BMP 时出错: {e}"

def bmp_to_jpg(input_path, output_path):
    """Converts BMP to JPG."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'jpeg')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 BMP 转换为 JPG 时出错: {e}"
