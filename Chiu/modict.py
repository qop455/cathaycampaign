# -*- coding: utf-8 -*-
"""
@author: jason
"""

from numpy import nan

def get_dummy_dict():
    result = dict()
    result['Region'] = {'E12000001':'NorthEast', 'E12000002':'NorthWest', 'E12000003':'YorkshireHumber', 'E12000004':'EastMidlands', 'E12000005':'WestMidlands', 'E12000006':'EastEngland', 'E12000007':'London', 'E12000008':'SouthEast', 'E12000009':'SouthWest', 'W92000004':'Wales'}
    result['Residence Type'] = {'C':'CommunalEstablishment', 'H':'NotCommunalEstablishment'}
    result['Family Composition'] = {1:'Family_NotInFamily', 2:'Family_Married', 3:'Family_Cohabiting', 4:'Family_LoneParentMale', 5:'Family_LoneParentFemale', 6:'Family_Other', -9:'NotRequired'}
    result['Population Base'] = {1:'PopulationBase_Usual', 2:'PopulationBase_StudentLivingAway', 3:'PopulationBase_ShortTime'}
    result['Sex'] = {1:'Sex_Male', 2:'Sex_Female'}
    result['Marital Status'] = {1:'MaritalStatus_Single', 2:'MaritalStatus_Married', 3:'MaritalStatus_Separated', 4:'MaritalStatus_Divorced', 5:'MaritalStatus_Widowed'}
    result['Student'] = {1:'Student', 2:'NotStudent'}
    result['Country of Birth'] = {1:'Birth_UK', 2:'Birth_NonUK', -9:'NotRequired'}
    result['Ethnic Group'] = {1:'EthnicGroup_White', 2:'EthnicGroup_Mixed', 3:'EthnicGroup_Asian', 4:'EthnicGroup_Black', 5:'EthnicGroup_ChineseOrOther', -9:'NotRequired'}
    result['Religion'] = {1:'Religion_NoReligion', 2:'Religion_Christian', 3:'Religion_Buddhist', 4:'Religion_Hindu', 5:'Religion_Jewish', 6:'Religion_Muslim', 7:'Religion_Sikh', 8:'Religion_Other', 9:'Religion_NotStated', -9:'NotRequired'}
    result['Economic Activity'] = {1:'EconomicActivity_Employee', 2:'EconomicActivity_SelfEmployed', 3:'EconomicActivity_Unemployed', 4:'EconomicActivity_FullTimeStudent', 5:'EconomicActivity_Retired', 6:'EconomicActivity_Student', 7:'EconomicActivity_LookingAfterHome', 8:'EconomicActivity_Disabled', 9:'EconomicActivity_Other', -9:'NotRequired'}
    result['Approximated Social Grade'] = {1:'SocialGrade_AB', 2:'SocialGrade_C1', 3:'SocialGrade_C2', 4:'SocialGrade_DE', -9:'NotRequired'}
    return result

def get_value_dict():
    result = dict()
    result['Age'] = {1:7.5, 2:20, 3:29.5, 4:39.5, 5:49.5, 6:59.5, 7:69.5, 8:75}
    result['Hours worked per week'] = {1:7.5, 2:23, 3:39.5, 4:49, -9:0}
    return result

def main():
    return

if __name__ == "__main__":
    main()
