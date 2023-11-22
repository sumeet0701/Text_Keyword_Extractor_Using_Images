import os 

def allowed_filename(filename):
    """
    This function is used to check whether a given filename has a allowed file extension
    """
    return '.'in filename and filename.rsplit('.', 1)[1].lower() in {'pdf','jpg','png','jpeg','gif'}

def save_uploaded_file(file):
    """
    This function is used to save a uploaded file to a specified directory if it has an allowed file extension
    """
    if file and allowed_filename(file.filename):
        filename = file.filename
        file.save(os.path.join('uploads', filename))
        return filename
    else:
        return None
    
    

