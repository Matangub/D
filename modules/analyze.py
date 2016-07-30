
from textblob import TextBlob
import modules.utils as utils

class Analyze:

    def __init__(self):
        self.sentences = []
        self.tokenizedParagraph = []

        print("started analyzing...")
        test = TextBlob("she couldn't convince him to give a speech")
        # print(test.sentences)

    # pushign new sentences into current state
    def pushText(self, text):
        newText = TextBlob(text)

        self.sentences = self.sentences + newText.sentences
        self.tokenizedParagraph = []

        for item in self.sentences:
            self.tokenizedParagraph.append( item.tags )

    def getLastSentence(self):
        return self.sentences[ len(self.sentences)-1 ]

    def getLastSentenceWithTags(self):
        return self.tokenizedParagraph[ len(self.tokenizedParagraph)-1 ] # last sentence in paragraph state

    def validateTokensInSentence(self, sentenceList, validateTokens):
        indexList = []
        for item in validateTokens:
            indexList.append( utils.index_containing_substring( sentenceList, item) )

        return utils.maxValidate(indexList)

    def searchTokenList(self, tokenList):
        lastSentence = self.getLastSentenceWithTags()# last sentence in paragraph state
        joinedTokens = []

        for index, item in enumerate(lastSentence):
            joinedTokens.append(lastSentence[index][1])

        print('lastSentence', lastSentence)
        print('tokenList', tokenList)
        # print('tokenList reversed', tokenList[::-1])

        ifFoundTokens = self.validateTokensInSentence(joinedTokens, tokenList)
        # ifFoundReversedTokens = self.validateTokensInSentence(joinedTokens, tokenList[::-1])
        print('ifFoundTokens', ifFoundTokens)
        # print('ifFoundReversedTokens', ifFoundReversedTokens)

        return ifFoundTokens

    def analyze(self):

        if( self.searchTokenList(['N', 'V']) and not self.searchTokenList(['V', 'N', 'V']) ):

            print(False, '1')
        elif self.searchTokenList(['N', 'W']) and not self.searchTokenList(['W', 'N', 'W']):

            print(False, '3')
        elif( self.searchTokenList(['PRP', 'MD', 'V']) ):

            print(False, '2')
        elif( self.searchTokenList(['W', 'V']) ):

            print("@1")
        elif( self.searchTokenList(['V', 'PRP']) ):

            print("@2")
        elif( self.searchTokenList(['MD', 'V'])):

            print("@3")
        elif( self.searchTokenList(['MD', 'PRP', 'V']) ):

            print("@4")
        else:
            print(False)
