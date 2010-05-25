T = {

    asyncUrls: {
        'subscribe': '/async/subscribe'
    },

    validateRegExp: {
      'mail': '^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$',
      'url' : '^[A-Za-z]+://[A-Za-z0-9-_]+\\.[A-Za-z0-9-_%&\?\/.=]+$'
    },

    errors: {
      '403': '对不起，请重新登录!'
    },

    //验证url
    validate: function(val, type) {
        var v = new RegExp();
        if(this.validateRegExp[type] == undefined){
            return false;
        }
        v.compile(this.validateRegExp[type]);
        if (!v.test(val)) {
            return false;
        }

        return true;
    },

    //通用alert 
    //TODO jquery ui
    alert: function(message, type) {
           alert(message);
    },

    //订阅
    subscribe: function(id) {
        var url = $.trim($('#' +id).val());
        if(url == ""){
            return this.alert($('#' + id).attr('empty'));                  
        }

        if(!this.validate(url, 'url')){
            return false;        
        }
        
        $.post(this.asyncUrls['subscribe'], {url:url}, function(data){
            if(data.error != 200){
                return T.alert(T.errors[data.error]);
            }

            if($('#feed_container').length == 0){
                return false;
            }
        
            if($('#feed_source_' + data.id).length > 0){
                return false;
            }

            var feed_source = '<li id="feed_source_' + data.id + '">' + data.url + '</li>';
            $('#feed_container').append($(feed_source));
        }, 'json');
    },
    
    //javascript 占位
    undef: function() {
        
    }
};
