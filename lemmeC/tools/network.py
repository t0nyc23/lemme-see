import dns.resolver as res
import requests

def internetdb(get_request, addresses):
    results = {}
    for addr in addresses:
        print(f"[+] Checking target addess: {addr} on InternedDB.")
        url = "https://internetdb.shodan.io/" + addr
        query = get_request(url)
        query_results = query.json()
        if "detail" not in query_results:
            results[str(addr)] = query_results

    return results

def get_addresses(domain):
    addresses = []
    answer = res.resolve(domain)
    #answer6 = res.resolve(domain, "AAAA")

    for val in answer:
        addresses.append(val.to_text())

    #for val6 in answer6:
    #    addresses.append(val6.to_text())

    return addresses

if __name__ == "__main__":
    get_request = requests.get
    target = input("> ")
    addresses = get_addresses(target)
    idb = internetdb(get_request, addresses)
