from PIL import Image

def ico_to_gif(input_path, output_path):
    """Converts ICO to GIF."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'gif')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 ICO 转换为 GIF 时出错: {e}"

def gif_to_ico(input_path, output_path):
    """Converts the first frame of a GIF to ICO."""
    try:
        img = Image.open(input_path)
        sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img.save(output_path, 'ico', sizes=sizes)
        return f"成功！图像的第一帧已保存到 {output_path}"
    except Exception as e:
        return f"从 GIF 转换为 ICO 时出错: {e}"
