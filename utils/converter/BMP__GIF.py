from PIL import Image

def bmp_to_gif(input_path, output_path):
    """Converts BMP to GIF."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'gif')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 BMP 转换为 GIF 时出错: {e}"

def gif_to_bmp(input_path, output_path):
    """Converts the first frame of a GIF to BMP."""
    try:
        img = Image.open(input_path)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        img.save(output_path, 'bmp')
        return f"成功！图像的第一帧已保存到 {output_path}"
    except Exception as e:
        return f"从 GIF 转换为 BMP 时出错: {e}"
