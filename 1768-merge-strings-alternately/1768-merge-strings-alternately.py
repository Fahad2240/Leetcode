class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        # print(temp)
        ans=""
        if len(word1)==len(word2):
            temp=""
            temp=temp+word1+word2
            front=0
            lst=len(temp)/2
            for x in range(0,len(temp)):
                if x%2==0:
                    ans=ans+temp[front]
                    front=front+1
                else:
                    ans=ans+temp[lst]
                    lst=lst+1
                if len(ans)==len(temp) or lst==len(temp) or front>len(temp)/2:
                    break
        elif len(word1)<len(word2):
            temp=""
            temp=temp+word1+word2[:len(word1)]
            print(temp)
            front=0
            lst=len(temp)/2
            for x in range(0,len(temp)):
                if x%2==0:
                    ans=ans+temp[front]
                    front=front+1
                else:
                    ans=ans+temp[lst]
                    lst=lst+1
                if len(ans)==len(temp) or lst==len(temp) or front>len(temp)/2:
                    break
            # return ans
            ans=ans+word2[len(word1):len(word2)]
        # print(ans)
        else:
            temp=""
            temp=temp+word1[:len(word2)]+word2
            print(temp)
            front=0
            lst=len(temp)/2
            for x in range(0,len(temp)):
                if x%2==0:
                    ans=ans+temp[front]
                    front=front+1
                else:
                    ans=ans+temp[lst]
                    lst=lst+1
                if len(ans)==len(temp) or lst==len(temp) or front>len(temp)/2:
                    break
            # return ans
            ans=ans+word1[len(word2):len(word1)]
        return ans
            