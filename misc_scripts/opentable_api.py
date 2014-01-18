import urllib2
import json
import sys

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

        #get responses
        #get response numbers

        restaurants = presponse['restaurants']

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
        query_url = rest_url + "?name="+rest_name
        area_key = "area"
        dc_value = "Washington, D.C. Area"

        response = urllib2.urlopen(query_url).read()
        presponse=json.loads(response)

        rest_list = list()

        restaurants = presponse['restaurants']
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
    params = {'city': 'Washington', 'name': 'matchbox'}
    reserv_url = test.getResevationURL(params,'2025480369',0)
    print reserv_url

    print ""
    print "TEST 2:"
    rlist = test.getRestaurants("matchbox")

    for item in rlist:
        print item


if __name__ == "__main__":
    sys.exit(main())