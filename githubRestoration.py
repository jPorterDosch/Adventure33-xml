import xml.etree.ElementTree as ET
import random
import os

def create_listener_element(listener_id):
    listener = ET.Element("listener", id=str(listener_id))
    ET.SubElement(listener, "ID").text = str(listener_id)
    ET.SubElement(listener, "IP").text = "1.1.1"
    ET.SubElement(listener, "UserAgent").text = "user agent"
    ET.SubElement(listener, "Referer").text = "https://ep2.adventure33.com:2112/SONGS"
    ET.SubElement(listener, "lag").text = "0"
    ET.SubElement(listener, "Connected").text = "8"
    return listener

def create_listener_file(mount_name):
    root = ET.Element("icestats")
    ET.SubElement(root, "admin").text = "webmaster@localhost"
    ET.SubElement(root, "banned_IPs").text = "0"
    ET.SubElement(root, "build").text = "20240429182102"
    ET.SubElement(root, "client_connections").text = "296267"
    ET.SubElement(root, "clients").text = "9"
    ET.SubElement(root, "connections").text = "296413"
    ET.SubElement(root, "file_connections").text = "711"
    ET.SubElement(root, "host").text = "ep2.adventure33.com"
    ET.SubElement(root, "listener_connections").text = "224"
    ET.SubElement(root, "listeners").text = "1"
    ET.SubElement(root, "location").text = "UK"
    ET.SubElement(root, "outgoing_kbitrate").text = "53"
    ET.SubElement(root, "server_id").text = "Icecast 2.4.0-kh15"
    ET.SubElement(root, "server_start").text = "29/Jun/2024:03:06:14 +0000"
    ET.SubElement(root, "source_client_connections").text = "35"
    ET.SubElement(root, "source_relay_connections").text = "0"
    ET.SubElement(root, "source_total_connections").text = "35"
    ET.SubElement(root, "sources").text = "6"
    ET.SubElement(root, "stats").text = "0"
    ET.SubElement(root, "stats_connections").text = "0"
    ET.SubElement(root, "stream_kbytes_read").text = "50122203"
    ET.SubElement(root, "stream_kbytes_sent").text = "602724"

    source = ET.Element("source", mount=mount_name)
    ET.SubElement(source, "artist").text = "unknown"
    ET.SubElement(source, "audio_codecid").text = "10"
    ET.SubElement(source, "connected").text = "113890"
    ET.SubElement(source, "genre").text = "various"
    ET.SubElement(source, "incoming_bitrate").text = "58216"
    ET.SubElement(source, "listener_connections").text = "14"
    ET.SubElement(source, "listener_peak").text = "4"
    ET.SubElement(source, "listeners").text = "1"
    ET.SubElement(source, "listenurl").text = f"http://ep2.adventure33.com:2112/{mount_name}"
    ET.SubElement(source, "max_listeners").text = "unlimited"
    ET.SubElement(source, "metadata_updated").text = "10/Jul/2024:13:26:21 +0000"
    ET.SubElement(source, "mpeg_channels").text = "1"
    ET.SubElement(source, "mpeg_samplerate").text = "22050"
    ET.SubElement(source, "outgoing_kbitrate").text = "182"
    ET.SubElement(source, "public").text = "0"
    ET.SubElement(source, "queue_size").text = "89881"
    ET.SubElement(source, "server_name").text = "no name"
    ET.SubElement(source, "server_type").text = "audio/aac"
    ET.SubElement(source, "slow_listeners").text = "0"
    ET.SubElement(source, "source_ip").text = "1.1.1"
    ET.SubElement(source, "stream_start").text = ""
    ET.SubElement(source, "title").text = ""
    ET.SubElement(source, "total_bytes_read").text = "816347044"
    ET.SubElement(source, "total_bytes_sent").text = "192962659"
    ET.SubElement(source, "total_mbytes_sent").text = "184"
    ET.SubElement(source, "user_agent").text = "user agent"
    ET.SubElement(source, "yp_currently_playing").text = ""

    for j in range(200):
        listener_id = random.randint(100000, 999999)
        listener_element = create_listener_element(listener_id)
        source.append(listener_element)

    root.append(source)
    file_name = f"{mount_name[1:]}listclients.xml"
    tree = ET.ElementTree(root)
    tree.write(file_name, encoding="UTF-8", xml_declaration=True)
    print(f"Generated {file_name}")

if __name__ == "__main__":
    for i in range(1, 101):
        mount_name = f"/FEED-{i}"
        create_listener_file(mount_name)