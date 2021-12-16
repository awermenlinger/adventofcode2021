# replicated from https://github.com/mebeim/aoc/blob/master/2021/README.md#day-16---packet-decoder
# had never done a bitstream decoding, this was a great learning experience
from math import prod

class Bitstream:
    def __init__(self, file):
        hexdata = file.read()
        rawdata = bytes.fromhex(hexdata)

        self.pos = 0
        self.bits = ''

        for byte in rawdata:
            self.bits += '{:08b}'.format(byte)
        
    def decode_int(self, nbits):
        res = int(self.bits[self.pos: self.pos+nbits], 2)
        self.pos += nbits
        return res
    
    def decode_one_packet(self):
        version = self.decode_int(3)
        tid = self.decode_int(3)
        data = self.decode_packet_data(tid)
        return (version, tid, data)
    
    def decode_value_data(self):
        value = 0
        group = 0b10000

        # 0b : indicates the next bits are an integer
        # & : bitwise compare if both 1 --> 1, else 0
        while group & 0b10000: #check that the group has a 1 has first bit, if not stop after last (group assigned in the loop)
            group = self.decode_int(5) # get the 5 bits
            value <<= 4 # add 4 0 bits at the end of value
            value += group & 0b1111 # only keep the 4 bits at the end of group and add them to value (they are all 0s)
        return value
    
    def decode_n_packets(self, n):
        return [self.decode_one_packet() for _ in range(n)] #generator to decode n packets in a row
    
    def decode_len_packets(self, length):
        end = self.pos + length   #when to stop
        pkts = []    # contains the packets

        while self.pos < end: # as long as the position is not the stop condition
            pkts.append(self.decode_one_packet()) #decode the one packet and move the position forward 3, 3, x * 5

        return pkts

    def decode_operator_data(self): 
        ltid = self.decode_int(1) # checks the first bit of operator packet 0 or 1

        if ltid == 1:
            data = self.decode_n_packets(self.decode_int(11)) # if first bit = 1, number of packets is 11 bits
        else:
            data = self.decode_len_packets(self.decode_int(15))   # if first bit = 1, number of packets is 15 bits

        return data

    def decode_packet_data(self, tid):  #operator or value packet
        if tid == 4:
            return self.decode_value_data()
        else:
            return self.decode_operator_data()

def sum_versions(packet):
    v, tid, data = packet

    if tid == 4:
        return v # if it's a value packet, there are no subpackets (no need to recurse)

    return v + sum(map(sum_versions, data)) #recursively find all the versions in the bitstream and sum them up
                                            #each of the subpacket is contained in data; map applies the f(x) to each
    


file = open("files\day16.txt", "r")
B = Bitstream(file)
packet = B.decode_one_packet() #get the top level packet
vsum = sum_versions(packet)

print("Part 1: ", vsum)

def evaluate(packet):
	_, tid, data = packet #capture tid for decision and either value or subpackets

	if tid == 4: #if value return value
		return data

	values = map(evaluate, data)  #call the evaluate function for all subpackets with this function

    #call subfunctions per values
	if tid == 0: return sum(values) 
	if tid == 1: return prod(values)
	if tid == 2: return min(values)
	if tid == 3: return max(values)

	a, b = values

	if tid == 5: return int(a > b)
	if tid == 6: return int(a < b)
	if tid == 7: return int(a == b)

	raise NotImplementedError('Unimplemented tid={}'.format(tid))

result = evaluate(packet)
print("Part 2: ", result)