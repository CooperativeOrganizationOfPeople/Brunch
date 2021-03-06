import urllib2
import json
import sys
import math

class opentable_api:

    # params- dict of key/value pairs, params for opentable API
    # phone_number- number of desired restaurant to match
    # mobile- '1' if on a mobile device (tablet/phone)
    # returns the reservation url, null string is error
    def getResevationURL(self,params,restaurant_phone,mobile):
        rest_url  = 'http://opentable.herokuapp.com/api/restaurants'
        #param_keys = params.viewkeys()
        #param_values = params.viewvalues()
        if len(params) < 1:
            return ""
        elif len(params) == 1:
            key,value = params.popitem()
            params_url = "?"+key+"="+value
        else:
            key,value = params.popitem()
            params_url = "?"+key+"="+value
            for key,value in params.iteritems():
                params_url = params_url+";"+key+"="+value
          
        query_url = rest_url +params_url
        response = urllib2.urlopen(query_url).read()

        presponse=json.loads(response)

        # Get the ceiling of total entries over the number of entries per page aka the number of pages
        pages = int(math.ceil(presponse['total_entries']/float(presponse['per_page'])))
        # Create the initial list of restaurants from the first page
        restaurants = presponse['restaurants']

        # If there is more than one page, request each page
        if pages > 1:
            pages = range(2,pages+1)
            for i in pages:
                page_query = query_url + ";page=" + str(i)
                response = urllib2.urlopen(page_query).read()
                presponse=json.loads(response)
                temp = presponse['restaurants']
                # For each item returned from additional pages append to the list of restaurants
                for j in temp:
                    restaurants.append(j)

        for item in restaurants:
            phone_num = item["phone"]
            if len(phone_num) > 10:
                phone_num = phone_num[:10]
            if phone_num == restaurant_phone:
                if mobile > 0:
                    return item["mobile_reserve_url"]
                else:
                    return item["reserve_url"]

    # Takes a potential restaurant name and searches opentable for restaurants by that name in the Washington DC area
    # Returns a list of restaurant names
    def getRestaurants(self,rest_name):
        rest_url  = 'http://opentable.herokuapp.com/api/restaurants'
        query_url = rest_url + "?name="+rest_name.replace(' ','')
        area_key = "area"
        dc_value = "Washington, D.C. Area"

        response = urllib2.urlopen(query_url).read()
        presponse=json.loads(response)

        rest_list = list()

        # Get the ceiling of total entries over the number of entries per page aka the number of pages
        pages = int(math.ceil(presponse['total_entries']/float(presponse['per_page'])))
        # Create the initial list of restaurants from the first page
        restaurants = presponse['restaurants']

        # If there is more than one page, request each page
        if pages > 1:
            pages = range(2,pages+1)
            for i in pages:
                page_query = query_url + ";page=" + str(i)
                response = urllib2.urlopen(page_query).read()
                presponse=json.loads(response)
                temp = presponse['restaurants']
                # For each item returned from additional pages append to the list of restaurants
                for j in temp:
                    restaurants.append(j)

        for item in restaurants:
            area = item[area_key]
            if area == dc_value:
                rest_list.append(item["name"])


        return rest_list

def main():
    #city = ';city=Washington'
    #name = '?name=matchbox'
    test = opentable_api()
    print "TEST 1:"
    #params = {'city': 'Washington', 'name': 'matchbox'}
    params = {'name': 'ted'}
    reserv_url = test.getResevationURL(params,'2025480369',0)
    print reserv_url

    print ""
    print "TEST 2:"
    rlist = test.getRestaurants("ted")

    for item in rlist:
        print item


if __name__ == "__main__":
    sys.exit(main())