// function searchOrder() {
//     // Perform API call to fetch order details based on the entered Order ID
//     // Fill the table body with the fetched data
//     document.getElementById('orderDetailsTable').classList.remove('hide');
//     document.getElementById('orderDetailsTable').classList.add('fadeIn');
// }


function showUpdateForm() {
    // Autofill form fields with the selected order details from the table
    document.getElementById('updateForm').classList.remove('hide');
    document.getElementById('updateForm').classList.add('fadeIn');
}

function openAddPO() {
$('#addPo').modal('show');


    
}
const addPo = new bootstrap.Modal(document.getElementById('addPo'), {
    backdrop: 'static',
    keyboard: false
    });
function openDtlPO(po_code) {
    $('#searchPO').modal('hide');
    $('#poDetails').modal('show');
    var xhr = new XMLHttpRequest();
    xhr.open('GET', `http://127.0.0.1:8000/api/po/${po_code}/`, true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {

            if (xhr.status === 200) {
                var data = JSON.parse(xhr.responseText);
                console.log(data);

                var dtl = `
    <p><strong>PO Number:</strong> ${data && data.po_number ? data.po_number : 'N/A'}</p>
    <p><strong>Vendor:</strong> ${data && data.vendor ? data.vendor : 'N/A'}</p>
    <p><strong>Order Date:</strong> ${data && data.order_date ? new Date(data.order_date).toLocaleString() : 'N/A'}</p>
    <p><strong>Delivery Date:</strong> ${data && data.delivery_date ? new Date(data.delivery_date).toLocaleString() : 'N/A'}</p>
    <p><strong>Items:</strong> ${data && data.items && data.items.length > 0 ? data.items[0].item_name : 'N/A'}</p>
    <p><strong>Quantity:</strong> ${data && data.quantity ? data.quantity : 'N/A'}</p>
    <p><strong>Status:</strong> ${data && data.status ? data.status : 'N/A'}</p>
    <p><strong>Quality Rating:</strong> ${data && data.quality_rating ? data.quality_rating : 'N/A'}</p>
    <p><strong>Issue Date:</strong> ${data && data.issue_date ? new Date(data.issue_date).toLocaleString() : 'N/A'}</p>
    <p><strong>Acknowledgment Date:</strong>${data && data.acknowledgment_date ? data.acknowledgment_date.toLocaleString() : 'N/A'}</p>
`;


                    var myDiv = document.getElementById('dtl');
                    myDiv.innerHTML=dtl            }
        }
    };
    xhr.onerror = function () {
        alert("Request failed"); // Handle network errors
    };
    xhr.send();

    }
function closeModal() {
// Close modal
this.hide();
}

function openSearch() {
$('#searchPO').modal('show');


}

const searchPO = new bootstrap.Modal(document.getElementById('searchPO'), {
    backdrop: 'static',
    keyboard: false
    });
// Open details modal on Details button click


const editPO = new bootstrap.Modal(document.getElementById('editPO'), {
backdrop: 'static',
keyboard: false
});

// Open details modal on Details button click
$('.detailsBtn').click(function() {
$('#detailsModal').modal('show');
});



        $(document).ready(function() {
            $('#myDataTable').DataTable();
        });

function openAddVendorDialog() {

    $('#addVendorModal').modal('show');
}
const addVendorModal = new bootstrap.Modal(document.getElementById('addVendorModal'), {
    backdrop: 'static',
    keyboard: false
});

function openSearchDialog() {
    $('#searchModal').modal('show');
}



function editPODialog(po_code) {
    $('#searchPO').modal('hide');

    document.getElementById('editPOLabel').innerHTML = po_code;

    var xhr = new XMLHttpRequest();
    xhr.open('GET', `http://127.0.0.1:8000/api/po/${po_code}/`, true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {

            if (xhr.status === 200) {
                var data = JSON.parse(xhr.responseText);
                console.log(data);
                var selectElement = document.getElementById("editvendor");

                for (var i = 0; i < selectElement.options.length; i++) {
                    console.log(selectElement.options[i].value );
                    console.log(data.vendor);
                    if (selectElement.options[i].value == data.vendor) {
                      selectElement.options[i].selected = true;
                      break; // Stop looping once the option is selected
                    }
                  }
                
                  document.getElementById('editpoid').value=po_code;
           
                document.getElementById('edititems').value = data.items[0].item_name
                document.getElementById("editqty").value = data.quantity

                $('#editPO').modal('show');
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


function openEditVendor(vendorid) {
    // $('#searchModal').modal('hide');
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
const editModal = new bootstrap.Modal(document.getElementById('editModal'), {
    backdrop: 'static',
    keyboard: false
});



const searchModal = new bootstrap.Modal(document.getElementByClas('searchModal'), {
    backdrop: 'static',
    keyboard: false
});




const details = new bootstrap.Modal(document.getElementById('detailsModal'), {
    backdrop: 'static',
    keyboard: false
});

function searchOrder() {


    var pocode = document.getElementById("orderIdInput1").value


    var xhr = new XMLHttpRequest();
    xhr.open('GET', `http://127.0.0.1:8000/api/po/${pocode}/`, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var data = JSON.parse(xhr.responseText);

                console.log(data);
                let table = ""
                var myDiv = document.getElementById('parent1');
                myDiv.removeChild(myDiv.children[1])



                table = ` <table class="table table-hover">
        <thead>
            <tr>
            <th scope="col">PO Number</th>
            <th scope="col">Vendor Name</th>
           
            <th scope="col">Edit List </th>
            <th scope="col">List Info</th>
            </tr>
        </thead>
        <tbody>

            <tr>
                <th scope="row">${data.po_number}</th>
                <td>${data.vendor}</td>

                <td>
                                        <button
                                            onclick="editPODialog('${data.po_number}');"
                                            class="btn btn-sm btn-primary editBtn"><i
                                                class="far fa-edit"></i>
                                            edit</button>
                                        <button
                                            onclick="deletePO('${data.po_number}');"
                                            class="btn btn-sm btn-danger deleteBtn"><i
                                                class="fas fa-trash-alt"></i>
                                            delete</button>
                                    </td>
                                    <td><button onclick="openDtlPO('${data.po_number}');"
                                            class="btn btn-sm btn-info detailsBtn"><i
                                                class="fas fa-info-circle"></i>
                                            Details</button></td>
            </tr>

        
        </tbody>
    </table>`
                var myDiv = document.getElementById('myDiv1');
                myDiv.insertAdjacentHTML('afterend', table);

            } else {
                console.error('There was a problem with the request.');
            }
        }
    };
    xhr.send();
}

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
                
                <a href="/performance-evaluation/${data.vendor_code}/">
                <button onclick="closeModal();" class="btn btn-sm btn-info detailsBtn">
                    <i class="fas fa-info-circle"></i> Details
                </button>
            </a>
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
function deletePO(po_code) {
    // $('#searchModal').modal('hide');
    // console.log("-----------------------------called");
    var xhr = new XMLHttpRequest();
    console.log(po_code);
    xhr.open('DELETE', `http://127.0.0.1:8000/api/po/${po_code}/`, true);
    xhr.onreadystatechange = function () {
        
        if (xhr.readyState === XMLHttpRequest.DONE) {
            alert(`${po_code} is Deleted`)
            location.href = "http://127.0.0.1:8000/purchase-order/"
        }
    }
    xhr.send();
}


