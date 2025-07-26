def read_logs(input_path):
    with open(input_path, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    return lines