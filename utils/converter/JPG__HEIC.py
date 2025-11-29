from PIL import Image
try:
    import pillow_heif
    pillow_heif.register_heif_opener()
    HEIF_SUPPORT = True
except ImportError:
    HEIF_SUPPORT = False

def jpg_to_heic(input_path, output_path):
    """Converts JPG to HEIC."""
    if not HEIF_SUPPORT:
        return "错误：HEIC 支持未安装。请运行 'pip install pillow-heif'。"
    try:
        img = Image.open(input_path)
        img.save(output_path, 'heic')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 JPG 转换为 HEIC 时出错: {e}"

def heic_to_jpg(input_path, output_path):
    """Converts HEIC to JPG."""
    if not HEIF_SUPPORT:
        return "错误：HEIC 支持未安装。请运行 'pip install pillow-heif'。"
    try:
        img = Image.open(input_path)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        img.save(output_path, 'jpeg')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 HEIC 转换为 JPG 时出错: {e}"
