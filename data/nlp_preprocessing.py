import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # 1. Build vocabulary: collect all unique words, sort them, assign integer IDs starting at 1
        # 2. Encode each sentence by replacing words with their IDs
        # 3. Combine positive + negative into one list of tensors
        # 4. Pad shorter sequences with 0s using nn.utils.rnn.pad_sequence(tensors, batch_first=True)
        words = []
        temp = positive[:]
        temp.extend(negative)

        for i in temp:
            word = i.split()
            for j in word:
                if(j not in words):
                    words.append(j)

        words.sort()
        encoded = []
        
        for i in temp:
            word = i.split()
            res = []
            for j in word:
                res.append(words.index(j)+1)
            
            encoded.append(torch.tensor(res))

        return nn.utils.rnn.pad_sequence(encoded,batch_first=True)



        
