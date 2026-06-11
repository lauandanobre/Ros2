# Ros2
## Esse é um repositório de códigos para robôs que utilizam a biblioteca ROS2


# Instruções

O pacote ROS2 está em `src/my_robot_controller`; o nó de exemplo fica em `src/my_robot_controller/my_robot_controller/my_first_node.py`.

Para usar, deve-se construir o workspace no diretório raiz:

```bash
source /opt/ros/humble/setup.bash
colcon build
```

Depois carregue o ambiente de instalação e em seguida execute o nó:

```bash
source install/setup.bash
ros2 run my_robot_controller my_first_node
```

Comandos principais usados:

- `source /opt/ros/humble/setup.bash`
- `colcon build`
- `source install/setup.bash`
- `ros2 run my_robot_controller my_first_node`

O workspace de exemplo está em `lau_ws`.
