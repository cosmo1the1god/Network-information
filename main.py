import subprocess


class NetworkInformation:

    def __init__(self):
        self.stdout = None
        self.stderr = None
        self.command = f"netsh wlan show profile key=clear"
        self.proc = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                     stderr=subprocess.PIPE, encoding='unicode_escape')

    def reading_command(self):
        self.stdout = self.proc.stdout.read().encode('utf-8')
        self.stderr = self.proc.stderr.read()

    def get_network_names(self):
        return self.stdout.decode('utf-8')

    @staticmethod
    def get_network_information():
        network_name = str(input(">which of the networks do you want enter the NAME: "))

        command_net = ['netsh', 'wlan', 'show', 'profile', 'name', '=', f"{network_name}", "key=clear"]

        proc = subprocess.Popen(command_net, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                stderr=subprocess.PIPE, encoding='unicode_escape')

        return proc.stdout.read()

    def automate(self):
        profile_names = self.get_network_names()
        profile_names = profile_names.split('Pro')
        listen = []
        if not profile_names:
            return None
        for i in range(len(profile_names)):
            listen.append(profile_names[i].split(':'))
        listen.pop(0)
        listen[0].pop(0)
        listen[0].pop(0)
        listen.pop(0)
        network_names = set()
        for b in range(len(listen)):
            for a in range(len(listen[b])):
                network_names.add(listen[b][1])

        for names in network_names:
            command_net = ['netsh', 'wlan', 'show', 'profile', 'name', '=', f"{names.strip()}", "key=clear"]
            print(command_net)
            proc = subprocess.Popen(command_net, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                    stderr=subprocess.PIPE, encoding='unicode_escape')
            return proc.stdout.read()   


if __name__ == '__main__':
    network = NetworkInformation()
    network.reading_command()
    print("NETWORK INFORMATION TOOL NETSH")
    option = str(input("""
Show Networks Name's [1]
Random Network PWD [2]\n\n>Chose you option: """))
    if option == '1':
        print(network.get_network_names())
        print(network.get_network_information())
    elif option == '2':
        print(network.automate())

