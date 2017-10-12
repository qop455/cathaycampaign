from numpy import nan

def get_dummy_dict():
    result = dict()
    result['Region'] = {'E12000001':'NorthEast', 'E12000002':'NorthWest', 'E12000003':'YorkshireHumber', 'E12000004':'EastMidlands', 'E12000005':'WestMidlands', 'E12000006':'EastEngland', 'E12000007':'London', 'E12000008':'SouthEast', 'E12000009':'SouthWest', 'W92000004':'Wales'}
    result['Residence Type'] = {'C':'CommunalEstablishment', 'H':'NotCommunalEstablishment'}
    result['Family Composition'] = {1:'NotInFamily', 2:'Married', 3:'Cohabiting', 4:'LoneParentMale', 5:'LoneParentFemale', 6:'Other', -9:'NotRequired'}
    result['Population Base'] = {1:'Usual', 2:'StudentLivingAway', 3:'ShortTime'}
    result['Sex'] = {1:'Male', 2:'Female'}
    result['Marital Status'] = {1:'Single', 2:'Married', 3:'Separated', 4:'Divorced', 5:'Widowed'}
    result['Student'] = {1:'Student', 2:'NotStudent'}
    result['Country of Birth'] = {1:'UK', 2:'NonUK', -9:'NotRequired'}
    result['Health'] = {1:'VeryGood', 2:'Good', 3:'Fair', 4:'Bad', 5:'VeryBad', -9:'NotRequired'}
    result['Ethnic Group'] = {1:'White', 2:'Mixed', 3:'Asian', 4:'Black', 5:'ChineseOrOther', -9:'NotRequired'}
    result['Religion'] = {1:'NoReligion', 2:'Christian', 3:'Buddhist', 4:'Hindu', 5:'Jewish', 6:'Muslim', 7:'Sikh', 8:'Other', 9:'NotStated', -9:'NotRequired'}
    result['Economic Activity'] = {1:'Employee', 2:'SelfEmployed', 3:'Unemployed', 4:'FullTimeStudent', 5:'Retired', 6:'Student', 7:'LookingAfterHome', 8:'Disabled', 9:'Other', -9:'NotRequired'}
    result['Approximated Social Grade'] = {1:'AB', 2:'C1', 3:'C2', 4:'DE', -9:'NotRequired'}
    return result

def get_value_dict():
    result = dict()
    result['Age'] = {1:7.5, 2:20, 3:29.5, 4:39.5, 5:49.5, 6:59.5, 7:69.5, 8:75}
    result['Hours worked per week'] = {1:7.5, 2:23, 3:39.5, 4:49, 5:0, -9:nan}
    return result

def main():
    return

if __name__ == "__main__":
    main()
