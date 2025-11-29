from PIL import Image
try:
    import pillow_heif
    pillow_heif.register_heif_opener()
    HEIF_SUPPORT = True
except ImportError:
    HEIF_SUPPORT = False

def png_to_heic(input_path, output_path):
    """Converts PNG to HEIC."""
    if not HEIF_SUPPORT:
        return "错误：HEIC 支持未安装。请运行 'pip install pillow-heif'。"
    try:
        img = Image.open(input_path)
        img.save(output_path, 'heic')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 PNG 转换为 HEIC 时出错: {e}"

def heic_to_png(input_path, output_path):
    """Converts HEIC to PNG."""
    if not HEIF_SUPPORT:
        return "错误：HEIC 支持未安装。请运行 'pip install pillow-heif'。"
    try:
        img = Image.open(input_path)
        img.save(output_path, 'png')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 HEIC 转换为 PNG 时出错: {e}"
