# Train the model
history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
