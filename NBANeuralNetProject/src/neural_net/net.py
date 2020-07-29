import learn
import preprocessing
import torch
import data_pull


optim = torch.optim.Adam(net.parameters(), lr =1e-4)

gameData = torch.tensor(data_pull.getGameData())
print(gameData.shape)

teamData = data_pull.getTeamData()



imagine= torch.tensor((10770, 2, 4))
losing = torch.tensor(())
data = imagine

net = learn.Net()
learn.train(net, optim, data, target)