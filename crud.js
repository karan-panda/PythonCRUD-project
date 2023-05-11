const api_url = "http://192.168.1.12:1234/users"
// const api_url = "http://192.168.249.221:1234/users"

function loadData(records = []) {
    var table_data = "";
        for(let i=0; i<records.length; i++) {
                table_data += `<tr>`;
                table_data += `<td>${records[i]['RollNo']}</td>`;
                table_data += `<td>${records[i]['FirstName']}</td>`;
                table_data += `<td>${records[i]['LastName']}</td>`;
                table_data += `<td>${records[i]['City']}</td>`;
                table_data += `<td>${records[i]['Age']}</td>`;
                table_data += `<td>${records[i]['ItemList']}</td>`;
                table_data += `<td>`;
                table_data += `<a href="edit.html?RollNo=${records[i]['RollNo']}"><button class="btn btn-primary">Edit</button></a>`;
                table_data += '&nbsp;&nbsp;';
                table_data += `<button class="btn btn-danger" onclick=deleteData('${records[i]['RollNo']}')>Delete</button>`;
                table_data += `</td>`;
                table_data += `</tr>`;
        }
        console.log(table_data);
        document.getElementById("tbody").innerHTML = table_data;
}

function getData(){
	fetch(api_url)
	.then((response) => response.json())
	.then((data) =>{
		loadData(data);
	});
}

function getDataByID(RollNo){
	fetch(`${api_url}edit?RollNo=${RollNo}`)
	.then((response) => response.json())
	.then((data) =>{
		console.log(data);
		document.getElementID("RollNo").value = data[0]['RollNo']
		document.getElementID("FirstName").value = data[0]['FirstName']
		document.getElementID("LastName").value = data[0]['LastName']
		document.getElementID("Age").value = data[0]['Age']
		document.getElementID("City").value = data[0]['City']
		document.getElementID("ItemList").value = data[0]['ItemList']
	});
}

function postData() {
        var RollNo = document.getElementById("RollNo").value;
        var FirstName = document.getElementById("FirstName").value;
        var LastName = document.getElementById("LastName").value;
        var Age = document.getElementById("Age").value;
        var City = document.getElementById("City").value;
        var ItemList = document.getElementById("ItemList").value;

        data = {RollNo: RollNo, FirstName: FirstName, LastName: LastName, Age: Age, City: City, ItemList: ItemList};

        fetch(api_url, {
                method: "POST",
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
        })
        .then((response) => response.json())
        .then((data) => {
                console.log(data);
                window.location.href = "index.html";
        })
}

function putData() {
        var RollNo = document.getElementById("RollNo").value;
        var FirstName = document.getElementById("FirstName").value;
        var LastName = document.getElementById("LastName").value;
        var Age = document.getElementById("Age").value;
        var City = document.getElementById("City").value;
        var ItemList = document.getElementById("ItemList").value;

        data = {RollNo: RollNo, FirstName: FirstName, LastName: LastName, Age: Age, City: City, ItemList: ItemList};

        fetch(api_url, {
                method: "PUT",
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
        })
        .then((response) => response.json())
        .then((data) => {
                console.log(data);
                window.location.href = "index.html";
        })
}

function deleteData(RollNo) {
        console.log(RollNo);
        user_input = confirm("Are you sure you want to delete this record?");
        if(user_input) {
                fetch(api_url+"?rollno="+RollNo, {
                        method: "DELETE",
                        headers: {
                          'Accept': 'application/json',
                          'Content-Type': 'application/json'
                        },
                        //body: JSON.stringify({"RollNo": RollNo})
                })
                .then((response) => response.json())
                .then((data) => {
                        console.log(data);
                        window.location.reload();
                })
        }
}
