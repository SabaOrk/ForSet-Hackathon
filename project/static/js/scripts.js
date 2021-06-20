<script >
						$(document).ready(function () {

							const cookies = document.cookie
    					.split(';')
    					.map(cookie => cookie.split('='))
    					.reduce((accumulator, [key, value]) => ({ ...accumulator, [key.trim()]: decodeURIComponent(value) }), {});

    					
    					function check_related(){
    						$.ajax({
                        data: {
                            'csrfmiddlewaretoken' : "{{ csrf_token }}",
                        }, // get the form data
                        url: "{% url 'check_relate' topic.pk %}",
                        type: 'POST',
                      
                        success: function(response) {
                            if (response.result === true) {
                                console.log('Related')
                                document.getElementById('relation_count').innerText = '{{topic.relation_count}} Can Relate'

                            }else if (response.result == false) {
                                console.log('UnRelated')
                                document.getElementById('relation_count').innerText = "{{topic.relation_count}} Can't Relate"
                            }

                        },
                        // on error
                        error: function(response) {
                            // alert the error if any error occured
                            console.log(response.responseJSON)
                        }
                    });
                return false;
    					}

    					check_related()

            // catch the form's submit event
            $('#relation_count').on('click', function () {
                // create an AJAX call
                $.ajax({
                        data: {
                            'csrfmiddlewaretoken' : "{{ csrf_token }}",
                        }, // get the form data
                        url: "{% url 'relate' topic.pk %}",
                        type: 'POST',
                      
                        success: function(response) {
                            if (response.result === true) {
                                console.log('Related')
                                console.log(response.count)

                                document.getElementById('relation_count').innerText = response.count + ' Can Relate'

                            }else if (response.result == false) {
                                console.log('UnRelated')
                                document.getElementById('relation_count').innerText = response.count + " Can't Relate"
                            }


                        },
                        // on error
                        error: function(response) {
                            // alert the error if any error occured
                            console.log(response.responseJSON)
                        }
                    });
                return false;
            });
        });
        $('#add_experience').on('click', function () {
                // create an AJAX call
                $.ajax({
                        data: {
                            'csrfmiddlewaretoken' : "{{ csrf_token }}",
                            'email':document.getElementById('email').value
                            'text':document.getElementById('text').value
                        }, // get the form data
                        url: "{% url 'add_experience' topic.title %}",
                        type: 'POST',
                      
                        success: function(response) {
                            if (response.result === true) {


                            }else if (response.result == 'Failed') {
                                console.log(response.result)
                            }

                        },
                        // on error
                        error: function(response) {
                            // alert the error if any error occured
                            console.log(response.responseJSON)
                        }
                    });
                return false;
            });

					</script>