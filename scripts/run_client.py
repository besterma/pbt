import argparse
import util

from client import PBTClient


def main(args):
    client = PBTClient(args.client_id, args.server_ip, args.server_port, args.auth_key)

    for _ in range(args.num_epochs):
        client.train_epoch()

        if client.exploit():
            client.explore()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # PBT Connection Settings
    parser.add_argument('--client_id', type=int, required=True,
                        help='ID of PBT client. Must be unique for each member of the population.')
    parser.add_argument('--server_ip', type=str, required=True,
                        help='IP address of PBT server.')
    parser.add_argument('--server_port', type=int, default=7777,
                        help='Port on which the server listens for clients.')
    parser.add_argument('--auth_key', type=str, default='insecure',
                        help='Key for clients to authenticate with server.')

    # Training Settings
    parser.add_argument('--num_epochs', type=int, default=10,
                        help='Number of epochs to train.')

    main(parser.parse_args())
