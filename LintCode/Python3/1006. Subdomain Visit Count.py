# Description
# A website domain like "discuss.lintcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "lintcode.com", and at the lowest level, "discuss.lintcode.com". When we visit a domain like "discuss.lintcode.com", we will also visit the parent domains "lintcode.com" and "com" implicitly.

# Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.lintcode.com".

# We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

# The length of cpdomains will not exceed 100.
# The length of each domain name will not exceed 100.
# Each address will have either 1 or 2 "." characters.
# The input count in any count-paired domain will not exceed 10000.
# The answer output can be returned in any order.
# Example
# Example 1:

# Input: 
# ["9001 discuss.lintcode.com"]
# Output: 
# ["9001 discuss.lintcode.com", "9001 lintcode.com", "9001 com"]
# Explanation: 
# We only have one website domain: "discuss.lintcode.com". As discussed above, the subdomain "lintcode.com" and "com" will also be visited. So they will all be visited 9001 times.

class Solution:
    """
    @param cpdomains: a list cpdomains of count-paired domains
    @return: a list of count-paired domains
    """
    def subdomainVisits(self, cpdomains):
        # Write your code here
        counter = {}
        for cpdomain in cpdomains:
            count, *domains = cpdomain.replace(' ','.').split('.')
            for i in range(len(domains)):
                domain = ".".join(domains[i:])
                counter[domain] = counter.get(domain, 0) + int(count)
        return [" ".join((str(v), k)) for k, v in counter.items()]