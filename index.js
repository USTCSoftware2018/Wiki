var app = new Vue({
    el: '#app',
    data: {
        message: 'hello world',
        rawHtml:'<span style="color:red">This should be red</span>'
    }
})

var app2 = new Vue({
    el: '#app-2',
    data:{
        message: 'load' + new Date().toLocaleString()
    }
})


var app3 = new Vue({
    el: '#app-3',
    data: {
        seen: false
    }
})

var app4 = new Vue({
    el: '#app4',
    data: {
        todos:[
            {name:'1',id:'haha'},
            {name:'2',id:'heihei'}
        ]
    }
})

var app5 = new Vue({
    el: '#app-5',
    data: {
        message: '123456'
    },
    methods: {
        reverse: function () {
            this.message = this.message.split('').reverse().join('')
        }
    }
})


var app6 = new Vue({

})