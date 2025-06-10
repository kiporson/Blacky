
def split_affiliate_link(base_url, user_id):
    return f"{base_url}?ref={user_id}"

def generate_affiliate_links(user_id, platforms):
    links = {}
    for platform in platforms:
        base_url = platforms[platform]
        links[platform] = split_affiliate_link(base_url, user_id)
    return links
