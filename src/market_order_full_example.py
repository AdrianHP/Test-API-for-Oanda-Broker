#!/usr/bin/env python

import argparse
import common.args
from order.view import print_order_create_response_transactions,print_orders
import v20
from pricing.view import price_to_string


def main():
    """
    Create a Market Order in an Account based on the provided command-line
    arguments.
    """

    parser = argparse.ArgumentParser()

    #
    # Add arguments for API connection
    #
    parser.add_argument(
        "--hostname",
        default="api-fxpractice.oanda.com",
        help="v20 REST Server hostname"
    )

    parser.add_argument(
        "--port",
        type=int,
        default=443,
        help="v20 REST Server port"
    )

    #
    # Add Account arguments
    #
    parser.add_argument(
        "101-001-27735311-001",
        help="v20 Account ID"
    )

    parser.add_argument(
        "02d75e69967ed14fc0c64dbbbedfc3fc-c2bd4eee5df7ac61a1cfef434df9977a",
        help="v20 Auth Token"
    )

    #
    # Add arguments for minimal Market Order
    #
    parser.add_argument(
        "EUR/USD",
        type=common.args.instrument,
        help="The instrument to place the Market Order for"
    )

    parser.add_argument(
        "10",
        help="The number of units for the Market Order"
    )
   
    # args = parser.parse_args()

    #
    # Create the API context based on the provided arguments
    #
    api = v20.Context(
       "api-fxpractice.oanda.com",
        443,
        token="02d75e69967ed14fc0c64dbbbedfc3fc-c2bd4eee5df7ac61a1cfef434df9977a"
    )

    #
    # Submit the request to create the Market Order
    #
    # response = api.order.market(
    #     "101-001-27735311-001",
    #     instrument="EUR_USD",
    #     units=-10
    # )
    
    response2 = api.order.list("101-001-27735311-001")
    
    # print_orders(response2)
    
   
   
   #.......Example for get a specific price.
    price_response = api.pricing.get("101-001-27735311-001",
                                     instruments = "EUR_USD")
    
    print(price_to_string( price_response.body['prices'][0]))
   #....
    
    #
    # Process the response
    #
    # print("Response: {} ({})".format(response.status, response.reason))

    # print("")

    # print_order_create_response_transactions(response)


if __name__ == "__main__":
    main()



