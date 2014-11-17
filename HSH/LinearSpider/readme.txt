[1]. What is LinearSpider

Suppose the data we need sit at the root of the URL tree. For example, the structure
looks like:

	Entrance
	|--- Country1 (reference information)
		|--- State1 (reference information)
			|--- City1 ===> target information
			|--- City2 ===> target information
			|--- City3 ...
		|--- State2
			...
	|--- Country2
		...

说明：
	为了解决这一类线性爬虫问题，我们把整个问题拆分成两步：
		1. 计划“任务树”。树的结构请在[2]中做了详细的介绍。
		2. 对根节点的URL运行爬虫，把数据储存在“数据树”json文件中。
		   树的结构在[3]中做了详细的介绍


[2]. Taskplanner.todo format

	{
		'URL1': 
				{
					'ref': { itemname: itemvalue,.= ...} <== what ever you get from url1
					'URL11':
							{
								'ref': { itemname: itemvalue,.= ...} <== what ever you get from url11
								'URL111': {...}
								'URL112': {...}
							}
					'URL12':{same as URL11}
				...
				}
		'URL2':{...}
		...
	}

说明：
	从入口URL开始，每一层URL下面应该有许多子URL，而当前URL下一定有一些参考信息可以为子URL所公用。
	所以'URL1'对应的值是一个自带'ref': {Referenceinfo} 的字典。然后我们把从URL1爬到的所有
	子URL都放到URL1的值中。每当我们爬子URL的时候，也以此类推。这样到最后就能形成一个树状的URL结构，
	而每一级的参考信息都被保存在了'ref': {}中。