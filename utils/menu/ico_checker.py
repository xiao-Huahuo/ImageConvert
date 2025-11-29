from PIL import Image

def get_ico_resolutions(file_path):
    """
    检查一个 ICO 文件并返回其包含的分辨率列表。

    Args:
        file_path (str): ICO 文件的路径。

    Returns:
        tuple: 一个元组 (success, message_or_data)。
               成功时，元组为 (True, [(width, height), ...])。
               失败时，元组为 (False, "错误信息")。
    """
    try:
        with Image.open(file_path) as img:
            if not hasattr(img, 'ico'):
                return False, "错误：文件不是有效的 ICO 格式。"
            
            sizes = img.ico.sizes()
            if not sizes:
                # 如果 .ico.sizes() 为空，可能是单帧ICO
                sizes = [img.size]
            return True, sorted(list(set(sizes)), key=lambda x: x[0])
    except FileNotFoundError:
        return False, "错误：文件未找到。"
    except Exception as e:
        return False, f"读取文件时出错: {e}"
