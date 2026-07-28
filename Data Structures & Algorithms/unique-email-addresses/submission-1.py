class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        my_set = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            my_set.add(local + '@' + domain)
    
        return len(my_set)
        

