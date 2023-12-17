function searchOrder() {
    // Perform API call to fetch order details based on the entered Order ID
    // Fill the table body with the fetched data
    document.getElementById('orderDetailsTable').classList.remove('hide');
    document.getElementById('orderDetailsTable').classList.add('fadeIn');
}

function deleteOrder() {

}

function updateOrder() {

}
function openAddVendorDialog() {

    $('#addVendorModal').modal('show');
}
const addVendorModal = new bootstrap.Modal(document.getElementById('addVendorModal'), {
    backdrop: 'static',
    keyboard: false
});

function closeModal() {
    // Close modal
    // $('#searchModal').hide(2000)
    this.hide
}

function openSearchDialog() {
    $('#searchModal').modal('show');
}



function openEditVendor(vendorid) {
    $('#searchModal').modal('hide');
    console.log("-----------------------------called");

    document.getElementById('editModalLabel').innerHTML = vendorid;

    var xhr = new XMLHttpRequest();
    xhr.open('GET', `http://127.0.0.1:8000/api/vendors/${vendorid}/`, true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {

            if (xhr.status === 200) {
                var data = JSON.parse(xhr.responseText);
                document.getElementById('name').value = data.name
                document.getElementById('contactDetails').value = data.contact_details
                document.getElementById('address').value = data.address
                document.getElementById("vcid").value = data.vendor_code

                $('#editModal').modal('show');
            } else {
                alert(`Error ${xhr.status}: ${xhr.statusText}`); // An error occurred!
            }
        }
    };
    xhr.onerror = function () {
        alert("Request failed"); // Handle network errors
    };
    xhr.send();
}


const searchModal = new bootstrap.Modal(document.getElementById('searchModal'), {
    backdrop: 'static',
    keyboard: false
});
// Open details modal on Details button click
// $('.editBtn').click(function () {
//     $('#editModal').modal('show');
// });


const editModal = new bootstrap.Modal(document.getElementById('editModal'), {
    backdrop: 'static',
    keyboard: false
});


const details = new bootstrap.Modal(document.getElementById('detailsModal'), {
    backdrop: 'static',
    keyboard: false
});



function searchUser() {


    var code = document.getElementById("orderIdInput").value


    var xhr = new XMLHttpRequest();
    xhr.open('GET', `http://127.0.0.1:8000/api/vendors/${code}/`, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var data = JSON.parse(xhr.responseText);

                console.log(data);
                let table = ""
                var myDiv = document.getElementById('parent');
                myDiv.removeChild(myDiv.children[1])



                table = ` <table class="table table-hover">
        <thead>
            <tr>
                <th scope="col">Vendor Code</th>
                <th scope="col">Vendor Name</th>
                <th scope="col">Edit List </th>
                <th scope="col">List Info</th>
            </tr>
        </thead>
        <tbody>

            <tr>
                <th scope="row">${data.vendor_code}</th>
                <td>${data.name}</td>
                <td>
                      
                        <button id="updatebtn" value="${data.vendor_code}"  onclick="openEditVendor('${data.vendor_code}')"
                            class="btn btn-sm btn-primary editBtn"><i
                                class="far fa-edit"  ></i>
                            edit</button>
                

                   
                        <button id="deletebtn"  value="${data.vendor_code}" onclick="deleteVendor('${data.vendor_code}')"
                            class="btn btn-sm btn-danger deleteBtn"><i
                                class="fas fa-trash-alt"></i>
                            delete</button>
                    </form>
                </td>
                <td>
                
                        <button  value="${data.vendor_code}" id ="detailsbtn"
                            class="btn btn-sm btn-info detailsBtn"><i
                                class="fas fa-info-circle"></i>
                            Details</button>
                
                </td>
            </tr>

        
        </tbody>
    </table>`
                var myDiv = document.getElementById('myDiv');
                myDiv.insertAdjacentHTML('afterend', table);

            } else {
                console.error('There was a problem with the request.');
            }
        }
    };
    xhr.send();
}

function deleteVendor(vendor_code) {
    $('#searchModal').modal('hide');
    console.log("-----------------------------called");
    var xhr = new XMLHttpRequest();
    console.log(vendor_code);
    xhr.open('DELETE', `http://127.0.0.1:8000/api/vendors/${vendor_code}/`, true);
    xhr.onreadystatechange = function () {
        
        if (xhr.readyState === XMLHttpRequest.DONE) {
            alert(`${vendor_code} is Deleted`)
            location.href = "http://127.0.0.1:8000/vendor-dtl/"
        }
    }
    xhr.send();
}