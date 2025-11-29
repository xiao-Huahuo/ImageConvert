import importlib
import os

MODULE_MAPPING = {
    frozenset(['jpg', 'jpeg']): 'JPG__JPEG',
    frozenset(['jpg', 'png']): 'JPG__PNG',
    frozenset(['jpeg', 'png']): 'JPEG__PNG',
    frozenset(['png', 'ico']): 'PNG__ICO',
    frozenset(['jpg', 'ico']): 'JPG__ICO',
    frozenset(['jpeg', 'ico']): 'JPEG__ICO',
    frozenset(['png', 'bmp']): 'PNG__BMP',
    frozenset(['jpg', 'bmp']): 'JPG__BMP',
    frozenset(['jpeg', 'bmp']): 'JPG__BMP',
    frozenset(['png', 'webp']): 'PNG__WEBP',
    frozenset(['jpg', 'webp']): 'JPG__WEBP',
    frozenset(['jpeg', 'webp']): 'JPG__WEBP',
    frozenset(['png', 'gif']): 'PNG__GIF',
    frozenset(['jpg', 'gif']): 'JPG__GIF',
    frozenset(['jpeg', 'gif']): 'JPG__GIF',
    frozenset(['png', 'heic']): 'PNG__HEIC',
    frozenset(['jpg', 'heic']): 'JPG__HEIC',
    frozenset(['jpeg', 'heic']): 'JPG__HEIC',
    frozenset(['png', 'svg']): 'PNG__SVG',
    frozenset(['jpg', 'svg']): 'JPG__SVG',
    frozenset(['jpeg', 'svg']): 'JPG__SVG',
    frozenset(['ico', 'bmp']): 'ICO__BMP',
    frozenset(['ico', 'webp']): 'ICO__WEBP',
    frozenset(['ico', 'gif']): 'ICO__GIF',
    frozenset(['ico', 'heic']): 'ICO__HEIC',
    frozenset(['ico', 'svg']): 'ICO__SVG',
    frozenset(['bmp', 'webp']): 'BMP__WEBP',
    frozenset(['bmp', 'gif']): 'BMP__GIF',
    frozenset(['bmp', 'heic']): 'BMP__HEIC',
    frozenset(['bmp', 'svg']): 'BMP__SVG',
    frozenset(['webp', 'gif']): 'WEBP__GIF',
    frozenset(['webp', 'heic']): 'WEBP__HEIC',
    frozenset(['webp', 'svg']): 'WEBP__SVG',
    frozenset(['gif', 'heic']): 'GIF__HEIC',
    frozenset(['gif', 'svg']): 'GIF__SVG',
    frozenset(['heic', 'svg']): 'HEIC__SVG',
}

def convert_image(input_path, output_path, output_format, output_filename):
    """
    Dynamically finds and calls the correct conversion function.
    """
    if not os.path.exists(input_path):
        return "错误：输入文件不存在。"

    input_ext = os.path.splitext(input_path)[1].lower().replace('.', '')
    output_ext = output_format.lower()

    if input_ext == output_ext:
        base_name_input = os.path.splitext(os.path.basename(input_path))[0]
        if base_name_input == output_filename:
            return "输入和输出格式及文件名均相同，无需转换。"

    key = frozenset([input_ext, output_ext])
    module_name = MODULE_MAPPING.get(key)

    if not module_name:
        reversed_key = frozenset([output_ext, input_ext])
        module_name = MODULE_MAPPING.get(reversed_key)

    if not module_name:
        if input_ext in ('jpg', 'jpeg') and output_ext in ('jpg', 'jpeg'):
             module_name = 'JPG__JPEG'
        else:
            return f"错误：不支持从 {input_ext} 到 {output_ext} 的转换路径。"

    function_name = f"{input_ext}_to_{output_ext}"

    try:
        converter_module = importlib.import_module(f".{module_name}", package="utils.converter")
        convert_func = getattr(converter_module, function_name)
        
        full_output_path = os.path.join(output_path, f"{output_filename}.{output_ext}")

        return convert_func(input_path, full_output_path)

    except ImportError:
        return f"错误：找不到实现文件 '{module_name}.py'。"
    except AttributeError:
        return f"错误：在模块 {module_name} 中找不到转换函数 '{function_name}'。"
    except Exception as e:
        return f"转换过程中发生未知错误：{e}"
