

## Determines the type of a single data point
def determine_type_with_index(data, start_index, end_index):

    if start_index == end_index or end_index < start_index:
        return 'B'

    temp_data = remove_whitespace(data[start_index:end_index])
    return determine_type(temp_data)

def determine_type(data):
    if any(c.isalpha() for c in data):
        return 'S'

    elif "." in data:
        return 'F'

    elif "-" in data:
        return 'I'

    elif data == "1" or data == "0":
        return 'B'


    elif not(any(c.isalnum() for c in data)):
        return 'B'

    else:
        return 'I'


## Removes the whitespace of a given data point
def remove_whitespace(data):
    return data.strip()
