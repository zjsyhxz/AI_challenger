# 数据说明

### 各csv文件内容
* train.csv 训练集数据
* validation.csv 验证数据集
* testa.csv 测试集A数据
* sample.csv 提交样例

### 数据标注说明
数据集分为训练、验证、测试A与测试B四部分。数据集中的评价对象按照粒度不同划分为两个层次，层次一为粗粒度的评价对象，例如评论文本中涉及的服务、位置等要素；层次二为细粒度的情感对象，例如“服务”属性中的“服务人员态度”、“排队等候时间”等细粒度要素。评价对象的具体划分如下表所示。  

<table>
	<tbody>
		<tr>
		  <td>层次一(The first layer)</td>
		  <td>层次二(The second layer)</td>
		</tr>
		<tr>
		  <td rowspan="3">位置(location)</td>
		  <td>
			  交通是否便利(traffic convenience)
		  </td>
		</tr>
		<tr>
		  <td>
			  距离商圈远近(distance from business district)
		  </td>
		</tr>
		<tr>
		  <td>
			  是否容易寻找(easy to find)
		  </td>
		</tr>
		<tr>
		<td rowspan="4">服务(service)</td>
		<td>
			排队等候时间(wait time)
		</td>
		</tr>
		<tr>
		  <td>
			  服务人员态度(waiter’s attitude)
		  </td>
		</tr>
		<tr>
		  <td>
			   是否容易停车(parking convenience)
		  </td>
		</tr>
		<tr>
		  <td>
			  点菜/上菜速度(serving speed)
		  </td>
		</tr>
		<tr>
		<td rowspan="3">价格(price)</td>
		<td>
			价格水平(price level)
		</td>
		</tr>
		<tr>
		  <td>
			性价比(cost-effective)
		  </td>
		</tr>
		<tr>
		<td>
			折扣力度(discount)
		</td>
		</tr>
		<tr>
		<td rowspan="4">环境(environment)</td>
		<td>
			装修情况(decoration)
		</td>
		</tr>
		<tr>
		  <td>
			  嘈杂情况(noise)
		  </td>
		</tr>  
		<tr>
		  <td>
			  就餐空间(space)
		  </td>
		</tr>  
		<tr>
		  <td>
			  卫生情况(cleaness)
		  </td>
		</tr>  
		<tr>
		<td rowspan="4">菜品(dish)</td>
		<td>
			分量(portion)
		</td>
		</tr>
		<tr>
		  <td>
			  口感(taste)
		  </td>
		</tr>
		<tr>
		  <td>
			  外观(look)
		  </td>
		</tr>
		<tr>
		  <td>
			  推荐程度(recommendation)
		  </td>
		</tr>
		<tr>
		<td rowspan="2">其他(others)</td>
		<td>
			本次消费感受(overall experience)
		</td>
		</tr>
		<tr>
		  <td>
			再次消费的意愿(willing to consume again)
		  </td>
		</tr>
	</tbody>
</table>

每个细粒度要素的情感倾向有四种状态：正向、中性、负向、未提及。使用[1,0,-1,-2]四个值对情感倾向进行描述，情感倾向值及其含义对照表如下所示：  

<table cellspacing="0">
	<tbody>
		<tr>
			<td>情感倾向值(Sentimental labels）</td>
			<td>1</td>
			<td>0</td>
			<td>-1</td>
			<td>-2</td>
		</tr>
		<tr>
			<td>含义（Meaning）</td>
			<td>正面情感(Positive)</td>
			<td>中性情感(Neutral)</td>
			<td>负面情感（Negative）</td>
			<td>情感倾向未提及（Not mentioned）</td>
		</tr>
	</tbody>
</table>

### 数据集下载协议

您（以下称“研究者”）正在请求举办方授予您访问、下载并使用数据集（以下简称“数据集”）的权利（以下简称“授权”），作为获得该等授权的条件，您同意遵守以下条款：

1. 研究者同意仅为非商业性的科学研究或课堂教学目的使用数据集，并不得将数据集用于任何商业用途；
2. 我们不享有数据集中使用的图片、音频、文字等内容的知识产权，对前述内容不作任何保证，包括但不限于不侵犯他人知识产权或可将前述内容用于任何特定目的；
3. 我们不承担因数据集使用造成的任何形式的损失或伤害，不会对任何因使用比赛数据产生的法律后果承担任何责任；
4. 与数据集使用有关的任何法律责任均由研究者承担，如研究者或其员工、代理人、分支机构使用数据集的行为给我们造成声誉或经济损失，研究者应当承担赔偿责任；
5. 研究者可以授权其助手、同事或其他合作者访问和使用数据集，但应确保前述人员已经认真阅读并同意接受本协议约束；
6. 如果研究者受雇于以盈利为目的的商业主体，应确保使用数据集仅用于非商业目的，且其雇主同样受本协议约束，研究者确认其签订本协议前已经取得雇主的充分授权。
7. 我们有权随时取消或撤回对研究者使用数据集的授权，并有权要求研究者删除已下载数据集；
8. 凡因本合同引起的或与本合同有关的任何争议，均应提交中国国际经济贸易仲裁委员会，按照申请仲裁时该会现行有效的仲裁规则，并适用中华人民共和国法律解决进行仲裁。仲裁语言应为中文。
