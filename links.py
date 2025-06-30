import urllib.parse
import json
import base64
import os

def parse_config_line(line):
    # Remove the leading and trailing symbols
    line = line.strip()
    if line.startswith('  - {'):
        line = line[5:].rstrip('}')
    elif line.startswith('- {'):
        line = line[3:].rstrip('}')
    elif line.startswith('{'):
        line = line[1:].rstrip('}')
    elif line.startswith('  -'):
        line = line[3:].strip()
    elif line.startswith('-'):
        line = line[1:].strip()

    config = {}
    parts = line.split(',')
    for part in parts:
        key_value = part.split(':', 1)
        if len(key_value) == 2:
            key = key_value[0].strip()
            value = key_value[1].strip().rstrip('}')  # Remove any trailing brace if present
            config[key] = value
    return config

def generate_ss_link(config):
    cipher = config.get('cipher', '')
    password = config.get('password', '')
    server = config.get('server', '')
    port = config.get('port', '')
    name = config.get('name', '')

    # Construct the part that needs to be base64 encoded
    encoded_part = f"{cipher}:{password}@{server}:{port}"
    # Base64 encode the part
    base64_encoded = base64.b64encode(encoded_part.encode()).decode()

    # Process the name to remove unwanted characters
    # Remove quotation marks if present
    if name.startswith('"') and name.endswith('"'):
        name = name[1:-1]

    # URL encode the name
    encoded_name = urllib.parse.quote(name)

    ss_link = f"ss://{base64_encoded}#{encoded_name}"
    return ss_link

def generate_vmess_link(config):
    vmess_config = {
        "v": "2",
        "ps": config.get('name', ''),
        "add": config.get('server', ''),
        "port": config.get('port', ''),
        "id": config.get('uuid', ''),
        "aid": config.get('alterId', '0'),
        "net": config.get('network', 'tcp'),
        "type": config.get('type', 'none'),
        "host": "",
        "path": "",
        "tls": config.get('tls', 'tls') == 'tls'
    }
    vmess_json = json.dumps(vmess_config)
    vmess_base64 = base64.b64encode(vmess_json.encode()).decode()
    return f"vmess://{vmess_base64}"

def generate_hysteria2_link(config):
    auth = config.get('auth', '')
    server = config.get('server', '')
    port = config.get('port', '')
    name = config.get('name', '')
    obfs = config.get('obfs', '')

    encoded_name = urllib.parse.quote(name)
    hysteria2_link = f"hysteria2://{auth}@{server}:{port}"
    if obfs:
        hysteria2_link += f"?obfs={obfs}"
    hysteria2_link += f"#{encoded_name}"
    return hysteria2_link

def generate_trojan_link(config):
    password = config.get('password', '')
    server = config.get('server', '')
    port = config.get('port', '')
    name = config.get('name', '')
    sni = config.get('sni', '')

    encoded_name = urllib.parse.quote(name)
    trojan_link = f"trojan://{password}@{server}:{port}"
    if sni:
        trojan_link += f"?sni={sni}"
    trojan_link += f"#{encoded_name}"
    return trojan_link

def main():
    config_lines = []
    print("请输入你的配置信息，每行一个配置。输入完成后，按 Enter 输入空行结束：")

    while True:
        line = input().strip()
        if not line:
            break
        config_lines.append(line)

    # Get desktop path
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    output_file_path = os.path.join(desktop_path, 'output_links.txt')

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in config_lines:
            config = parse_config_line(line)
            protocol = config.get('type', '').strip().lower()

            if protocol == 'ss':
                link = generate_ss_link(config)
            elif protocol == 'vmess':
                link = generate_vmess_link(config)
            elif protocol == 'hysteria2':
                link = generate_hysteria2_link(config)
            elif protocol == 'trojan':
                link = generate_trojan_link(config)
            else:
                link = "Unsupported protocol: " + protocol

            print(link)
            output_file.write(link + '\n')

    print(f"链接已保存到桌面的 output_links.txt 文件中。")

if __name__ == "__main__":
    main()
