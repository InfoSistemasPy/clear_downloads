import shutil
import os


def extension_type(event):
    return event.src_path[event.src_path.rindex('.') + 1:]


def is_text_file(event):
    if extension_type(event) == 'txt' or 'doc' or 'docx' or 'xls' or 'ppt':
        return True
    return False


def is_pdf_file(event):
    if extension_type(event) == 'pdf':
        return True
    return False


def is_mp3_file(event):
    if extension_type(event) == 'wma' or 'mp3' or 'wma' or 'aac' or 'ogg' or 'ac3' or 'wav':
        return True
    return False


def is_image_file(event):
    if extension_type(event) in ('png', 'jpg', 'jpeg', 'bmp', 'gif', 'raw'):
        return True
    return False


def is_video_file(event):
    if extension_type(event) in ('mov', 'mp4', 'avi', 'flv', 'MPEG', 'RMVB ', 'MKV'):
        return True
    return False


def is_doc_file(event):
    if extension_type(event) in ('doc', 'docx'):
        return True
    return False


def is_spreadsheet_file(event):
    if extension_type(event) in ('xls', 'xlsx'):
        return True
    return False


def is_presentation_file(event):
    if extension_type(event) in ('ppt', 'pptx'):
        return True
    return False


def is_code_file(event):
    if extension_type(event) in ('py', 'cs', 'js', 'php', 'html', 'sql', 'css'):
        return True
    return False


def is_executable_file(event):
    if extension_type(event) in ('exe', 'msi', 'apk', 'jar'):
        return True
    return False

def is_compact_file(event):
    if extension_type(event) in ('zip', 'rar', 'iso', '7z'):
        return True
    return False

def is_torrent_file(event):
    if extension_type(event) in ('torrent'):
        return True
    return False

def make_folder(foldername):
    os.chdir('C:/Users/thiago/Downloads')
    if os.path.exists(foldername) == True:
        print('A pasta já existe, pulando a criação')
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)


def move_to_new_corresponding_folder(event, path_to_new_folder):
    try:
        shutil.move(event.src_path, path_to_new_folder)
        print('arquivo em movimento')
    except:
        print('O arquivo já existia na pasta de destino')
        pass
