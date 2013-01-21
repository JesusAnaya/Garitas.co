$(document).on('ready', function(){
    $('#box_popup').hide();

    /*
     * Models
     */
    var Border = Backbone.Model.extend({
        urlRoot: $("meta[name='border-model']").attr('content')
    });

    /*
     * Collections
     */
    window.BorderCollection = Backbone.Collection.extend({
        model: Border,
        url: $("meta[name='border-model']").attr('content')
    });

    /*
     * Views
     */
    window.BorderListView = Backbone.View.extend({
        el: $("#border-ports"),
        template: Mustache.template('border'),

        initialize: function(){
            this.collection = new BorderCollection();
            this.collection.bind("reset", this.render, this);
            this.collection.bind("change", this.render, this);
            this.collection.bind("add", this.render, this);

            this.collection.fetch();
        },

        render: function(eventName){
            $(this.el).empty();
            _.each(this.collection.models, function (border){
                $(this.el).append(this.template.render({
                    'port': border.toJSON()
                }));
            }, this);
        }
    });

    border_list_view = new BorderListView();
});
