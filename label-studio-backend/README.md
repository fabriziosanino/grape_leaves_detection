# Label studio backend

## Start backend (model.py)
1. Insert into the path *data/server/models/* the model that the backend should use
2. Modify the **MODEL_FILE_NAME** constants with the name of the model file
3. In the *docker-compose.yaml* set **LABEL_STUDIO_URL** and **LABEL_STUDIO_API_KEY** with the proper values. For the **LABEL_STUDIO_API_KEY** you need to go in your label-studio Account&Settings and get the Access Token
4. Run *docker-compose up* for create and execute the container

(!) If you want to modify something, you need to delete the container and the image, then perform 3. Also, you have to insert the correct requirements in the *requirements.txt* folder

## Connect label-studio to the backend 
1. Open the desired project on label-studio
2. Go to **settings** then **Machine Learning**
3. Click **Add Model** and insert *http://ip_of_your_pc:port*. The port is the one which the container previously created is listening. By default is **9090**.
4. Enable the *Use for interactive preannotations* option and click **Validate and Save**. (!) The first time it fails because the backend needs to download additional packages so the timeout expires. Wait 20 sec then click **Validate and Save**. Now should work. 
5. In  the **settings** page go to **Labelling Interface** and select **Code** view. Insert to the desired label (the one which will be automatically labeled by the backend. The must have the same name of the back one) the following attributes: *smart="true"* and *showInline="true"*

Now when clicking on a new image, the backend should predict the bboxes for the selected images.


