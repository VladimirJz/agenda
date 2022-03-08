class Widgets():
    def Breadcrumb(self):
        '''Return a dic whit name/url pair'''
        view_name=self.request.resolver_match.url_name
        choices=view_name.split("_")
        path=''
        breadcrumb = dict()
        items=(len(choices)-1)
        for i, option in enumerate(choices):
            #path=path + option + '_'
            #breadcrumb[path[:-1]] = option
            if i==items:
                path='#_'
            else:
                path=path+option+'_'
            breadcrumb[path[:-1]]=option
        return breadcrumb
    def Timeline(self):
        pass