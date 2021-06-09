import pymongo


class MongodbPipeline(object):
    collection_name = 'best_movies'
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://pankaj:Toptal@21@cluster0.cso4b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client["IMDB"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
