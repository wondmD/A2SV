class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_map = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            subdomains = domain.split('.')
            
            temp = ''
            for i in range(len(subdomains) - 1, -1, -1):
                if temp == '':
                    temp = subdomains[i]
                else:
                    temp = subdomains[i] + '.' + temp
                
                if temp in count_map:
                    count_map[temp] += int(count)
                else:
                    count_map[temp] = int(count)
        
        result = []
        for subdomain, count in count_map.items():
            result.append(str(count) + ' ' + subdomain)
        
        return result