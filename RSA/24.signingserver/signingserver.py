from Cryptodome.Util.number import long_to_bytes
N=0xac75f79fce92e1da50ca29668757467e2af8809f2474477e6635367bef04ea476e303bbfffc98b190d47fa17e5588925121f5a973f1078ce20741c13859af0f7542ebf8fcd5c1bad29b08eeada9aba6a7e40bffe61bc9f8f3e2e3b9fba18ea5ffe31c8316567aa989f763726b05e2533eb8750fb17af065040bf3662a700bdc54b75dbfce7624dded6b3ffe3a710ddb2183b45cba06f4858389e147ac907b26bfa752190bcfdc3eed9b1589bd034d4dbf8d53a5a83d74032ee2349b779c5ea9b98f0791c875bdeff5022254ddfe5d4b0e1f9bb606fd725e5b77484964c00a10dea4ab4dac4c1afe79777ed8ff9cdc635daced77b94713cc5d2e99f25e8fa3187
e=0x10001
secret=0x36616f25259cd2f073ce920144b1054d891fcd20cf243c4fc0bac556b5d7240fe92d8a19db7cfcee183c64f29585226521189b3d1c8be02d79ee754856cf1efae8a136cb02e045edd3f44b704a759f756574db89571b4b2fc3e52258ff15224e93072360afd7cea95d81029bc59f400dc1492597b958b8183c87a07a909b7ab407d44e5f65875e8b94585bbc60662a022e0c5edb18a28746ead4b8f8247cb80012d53a04ffa720cb10de0927f21a1334a49f5dae246d659672f8ff27703a52412dc9291f4ea50edd0d53a61cd8032336b3e416496bf2c424154018d2793c2d778c83fc245d8fabad2053d3e77767ba0feb3c094887e5424efbf5c5f02f618ec5
sign=0x544f444f3a206175646974207369676e696e672073657276657220746f206d616b6520737572652074686174206d6564646c696e67206861636b657220646f65736e27742067657420686f6c64206f66206d792073656372657420666c61673a2063727970746f7b64306e375f3531366e5f6a7535375f346e793768316e367d
print(long_to_bytes(sign))

