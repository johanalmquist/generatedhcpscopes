import csv
from netaddr import IPNetwork
from jinja2 import Environment, FileSystemLoader

class Ranges:
    # initial variables
    csv_file:str
    outputFile:str
    networks = []
    gateway: str = "1"
    start_range: str = "2"
    end_range: str = "254"
    primaryDNS:str = "8.8.8.8"
    secondaryDNS:str = "8.8.4.4"

    # Set path where csv is saved
    def setPathToCsvFile(self, filePath:str):
        self.csv_file = filePath
    
    # Set where to save output file
    def setPathToSaveOutputFile(self, filePath:str):
        self.outputFile = filePath

    # To write over default value for gateway
    def setGateway(self, gateway:str):
        self.gateway = gateway

    # To write over default value for start address in range
    def setStartRange(self, start_range:str):
        self.start_range = start_range
    
    # To write over default value for end address in range
    def setEndRange(self, end_range:str):
        self.start_range = end_range

    # To write over default value for primaryDNS
    def setPrimaryDNS(self, primaryDNS:str):
        self.primaryDNS = primaryDNS
    
    # To write over default value for secondaryDNS
    def setSecondaryDNS(self, secondaryDNS:str):
        self.secondaryDNS = secondaryDNS

    # Set first aviable ip for subnet scope scope
    def __makeStartRange(self, ip:str):
        ip = ip.split('.')
        ip[3] = self.start_range
        start = ".".join(ip)
        return start

    # Set last aviable ip for subnet scope
    def __makeEndRange(self, ip:str):
        ip = ip.split('.')
        ip[3] = self.end_range
        end = ".".join(ip)
        return end

    # Set gateway aviable ip for subnet
    def __makeGateway(self, ip:str):
        ip = ip.split('.')
        ip[3] = self.gateway
        gateway = ".".join(ip)
        return gateway
    
    # Read data from csv file and save the subnet to a dict
    def filterNetworks(self):
        with open(self.csv_file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Skip first line in csv_file
            next(csv_reader)
            for line in csv_reader:
                ip_range = IPNetwork(line[1])
                #print(dir(ip_range.network))
                self.networks.append({
                                    'site':line[0], 
                                    'ip':ip_range.network, 
                                    'mask':ip_range.netmask, 
                                    'broadcast':ip_range.broadcast,
                                    'gateway':self.__makeGateway(str(ip_range.network)),
                                    'start_range':self.__makeStartRange(str(ip_range.network)),
                                    'end_range':self.__makeEndRange(str(ip_range.network)),
                                    'primaryDNS':self.primaryDNS,
                                    'secondaryDNS':self.secondaryDNS
                                })
    # Genratre output file with dhcp scope for every subnets in the csv file
    def generate(self):
        self.filterNetworks()
        # Tell jinj2 engige the folder that holds templates file
        env = Environment(loader=FileSystemLoader('templates'))
        # Tell jinj2 enegige with template file to use
        template = env.get_template('scopes.html')
        # Render scopes in template file and passdown the list with subnets
        # and save it to a variable
        output_from_template = template.render(networks=self.networks)
        # Save the outout from the output file to a txt file
        with open(self.outputFile, "w") as file:
            file.write(output_from_template) 
        
        


