class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        count=0
        
        while True:
            for i in range(len(tickets)):
                if tickets[i]==0:
                     continue 
                tickets[i]-=1
                count+=1
                if  tickets[k]==0:
                   return count
                   



        