import re

def rename_disc_to_part(invalid_filename):
    # Match filenames ending with (Disc x) and rename to .partx
    match = re.search(r'^(.*)\(Disc (\d+)\)$', invalid_filename)
    if match:
        base_name = match.group(1).strip()
        disc_number = match.group(2)
        return f"{base_name}.part{disc_number}"
    return invalid_filename

def reorder_the_in_title(invalid_filename):
    # Match filenames with the format "Title, The" and rename to "The Title"
    match = re.search(r'^(.*?), The(.*)$', invalid_filename)
    if match:
        base_name = match.group(1).strip()
        rest = match.group(2)
        return f"The {base_name}{rest}"
    return invalid_filename

def remove_unwanted_tags(invalid_filename):
    # Define the specific unwanted patterns inside parentheses
    patterns = [
        r'\(U\)',
        r'\(En,Fr,De,Es,It\)',
        r'\(Europe\)',
        r'\(M\d+\)',
        r'\(Proto\)',
        r'\(\d{4}-\d{2}-\d{2}\)',
        r'\(USA\)',
        r'\(World\)',
        r'\(NDSi Enhanced\)',
        r'\(PSP\)',
        r'\(PSN\)',
        r'\(CGB\+SGB Enhanced\)',
        r'\(Demo\)',
        r'\(DSi Enhanced\)',
        r'\(E\)',
        r'\(En,Fr,De\)',
        r'\(En,Fr,De,Es\)',
        r'\(En,Fr,De,Es,It,Nl,Pt,Sv\)',
        r'\(En,Fr,De,Es,It,Nl,Sv\)',
        r'\(En,Fr,De,It\)',
        r'\(En,Fr,Es\)',
        r'\(EU\)',
        r'\(Europe\)',
        r'\(FR\)',
        r'\(France\)',
        r'\(Japan\)',
        r'\(Japan, USA\)',
        r'\(Kiosk\)',
        r'\(Mindscape\)',
        r'\(NTSC\)',
        r'\(Promo\)',
        r'\(Rev \d+\)',
        r'\(SGB Enhanced\)',
        r'\(UE\)',
        r'\(Unl\)',
        r'\(USA, Asia\)',
        r'\(USA, Europe\)',
        r'\(v\d+(\.\d+)*\)',  # Matches versions like (v1), (v1.2), (v1.2.3)
        r'\(V\d+(\.\d+)*\)'   # Matches versions like (V1), (V1.2), (V1.2.3)
    ]

    # Remove unwanted patterns
    for pattern in patterns:
        invalid_filename = re.sub(pattern, '', invalid_filename).strip()

    return invalid_filename

def remove_square_bracketed_content(invalid_filename):
    # Remove content enclosed in square brackets
    return re.sub(r'\[.*?\]', '', invalid_filename).strip()

def remove_unnecessary_spaces(invalid_filename):
    # Remove leading, trailing, and multiple consecutive spaces
    filename = re.sub(r'\s+', ' ', invalid_filename).strip()
    # Remove spaces before .partX
    filename = re.sub(r'\s+\.part', '.part', filename)
    return filename
