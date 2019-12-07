$(function () {
    $("#tree").fancytree({
        activeVisible: false,
        autoActivate: false,
        autoCollapse: false,
        autoScroll: false,
        clickFolderMode: 2,
        debugLevel: 2,
        extensions: ["filter"],
        filter: {
            counter: false,
            mode: "hide"
        },
        selectMode: 1,
        click: function(event, data) {
            if (data.node.isFolder() == false && typeof data.node.data.src !== 'undefined') {
                var $videotitle = $("#videotitle");
                var $videoplayer = $("#videoplayer");
                $videotitle.text(data.node.data.name);
                $videoplayer.attr("src", data.node.data.src);
            }
        }
    });
    
    var $treeFilter = $("#treeFilter");
    var $tree = $.ui.fancytree.getTree("#tree");
    $treeFilter.keyup(function() {
        var txt = $treeFilter.val();
        if (txt !== "") {
            $tree.filterNodes(txt);
        }
        else {
            $tree.clearFilter();
        }
    });

});