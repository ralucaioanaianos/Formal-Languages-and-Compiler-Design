package ro.ubb.lab11.core.repository;

import ro.ubb.lab11.core.model.Airplane;

import java.util.List;

public interface IAirplaneRepository extends IRepository<Airplane, Long>{
    List<Airplane> findAllByModel(String model);
    List<Airplane> findAllByOrderByAgeAsc();

}
