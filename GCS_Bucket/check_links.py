import requests

working_links=[]

with open("links.txt", "r") as linkFile:
    links = linkFile.readlines()
    total_links = len(links)
    print("Total links: " + str(total_links))
    current_count = 0
    for link in links:
        current_count += 1
        if(current_count % 30 == 0 and current_count > 0):
            print(f'Total {current_count} links visited')
        link = link.strip()
        try:
            response = requests.get(link)
            
            if(response.status_code == 200):
                json_data = response.json()
                if "items" in json_data and len(json_data["items"]) > 0:
                    # we are not iterating through all the mediaLinks, just checking
                    # if the bucket is open and accessible
                    media_link = json_data["items"][0].get("mediaLink")
                    content_type = json_data["items"][0].get("contentType")
                    media_link_response = requests.get(media_link)
                    if media_link_response.status_code == 200:
                        print(media_link, content_type)
                        working_links.append([link, media_link, content_type])
                        
        except Exception as e:
            print(f'{str(e)}')


with open("working_links.txt", "w") as workLinkFile:
    for link in working_links:
        workLinkFile.write(link[0] + " " + link[1] + " " + link[2])
